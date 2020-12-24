抽象类不允许被直接创建对象，其他类的特性依旧存在。抽象类的实现应在继承该类的子类中去具体实现。抽象类中只负责定义该抽象方法。由于abstract 的方法需要在继承后的子类中实现，因此不可以 与final , private , static 共存。

## Dependency inversion principle 依赖反转原则
    抽象不应该依赖于具体实现，具体实现应该依赖于抽象
    High-level的实体不应该依赖于low-level的实体