package main

import (
	"context"
	"fmt"
	"net/http"
)

type UserDataStore interface {
	GetUserScore(ctx context.Context, id string) (int, error)
	DeleteUser(ctx context.Context, id string) error
}

func GetUserScoreHandler(userDataStore UserDataStore) http.HandlerFunc {
	return func(res http.ResponseWriter, req *http.Request) {
		id := req.Header.Get("x-user-id")
		score, err := userDataStore.GetUserScore(req.Context(), id)
		if err != nil {
			fmt.Println("userDataStore.GetUserScore: ", err)
			res.WriteHeader(http.StatusInternalServerError)
			return
		}
		res.Write([]byte(fmt.Sprintf("%d", score)))
	}
}

type mockUserDataStore struct {
	pendingError error
	pendingScore int
}

func (m *mockUserDataStore) GetUserScore(ctx context.Context, id string) (int, error) {
	return m.pendingScore, m.pendingError
}

func (m *mockUserDataStore) DeleteUser(ctx context.Context, id string) error {
	return nil
}

func main() {
	mockStore := &mockUserDataStore{
		pendingScore: 42,
	}
	http.HandleFunc("/user-score", GetUserScoreHandler(mockStore))

	fmt.Println("Server listing on :8080")
	http.ListenAndServe(":8080", nil)
}
