from main import Add

def TestAdd():
    assert Add(2,3) == 5
    assert Add(5,5) == 10
    print("Add Function works correctly and it works")

if __name__ == '__main__':
    TestAdd()