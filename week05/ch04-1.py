## 클래스와 함수 선언 부분 ##

class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start

    if current is None:
        return

    print(current.data, end=' ')

    while current.link is not None:
        current = current.link
        print(current.data, end=' ')

    print()


def insertNode(findData, insertData):
    global memory, head, current, pre

    # 첫 번째 노드 삽입
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return

    # 중간 노드 삽입
    current = head

    while current.link is not None:
        pre = current
        current = current.link

        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return

    # 마지막 노드 삽입
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)


## 전역 변수 선언 부분 ##

memory = []
head, current, pre = None, None, None

dataArray = ["다현", "정연", "쯔위", "사나", "지효"]


## 메인 코드 부분 ##

if __name__ == "__main__":

    # 첫 번째 노드 생성
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    # 두 번째 이후 노드 생성
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    # 초기 연결 리스트 출력
    printNodes(head)

    # 첫 번째 노드 삽입
    insertNode("다현", "화사")
    printNodes(head)

    # 중간 노드 삽입
    insertNode("사나", "솔라")
    printNodes(head)

    # 마지막 노드 삽입
    insertNode("재남", "문별")
    printNodes(head)