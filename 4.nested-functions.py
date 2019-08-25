def parent():
    print("This is from parent")
    def child1():
        print("This is from child1")
        def child2():
            print("This is from child2")
        child2()
    
    child1()

parent()