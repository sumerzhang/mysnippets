### Go 中的 Interface 接口

在 Go 语言中， 接口（interface) 是一个方法签名的集合。它通常定义一个类型（type)应该表现的一组行为。和传统的面向对象的语言不一样的，Go 的接口是隐式实现。这意味着任何类型只要实现接口定义的方法，就会自动实现这个接口。

#### 什么时候使用接口？

1. 解耦和依赖翻转（decoupling and dependency inversion)
   接口通常用来解耦代码，通过定义接口，可以实现依赖翻转，并且是代码更加可维护
2. 可测试性
   接口可以增加程序的可测试性。你可以方便的 mock 实现达到测试的目的。

下面是一个简单的示例

```rust
macro_rules! say_hello {
  () => {
    println!("Hello, world!");
  };
}

fn main() {
  say_hello!(); //这里调用宏
}
```

复杂点的例子
```rust
# [allow(unused)]
macro_rules! calculate {
    (eval $e:expr) => {
        let val: usize = $e;
        println!("{} = {}", stringify!($e), val);
    }
}

fn main() {
    calculate! {
        eval 1 + 2
    }
    calculate! {
        eval (1 + 2) * (3 + 4)
    }
}
```
