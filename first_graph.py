import operator
from typing import Annotated, List, Literal, TypedDict
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class State(TypedDict):
    nlist: List[str]


def node_a(state: State) -> State:
    print(f"in node a getting {state['nlist']}")
    note = "ho ho ho"
    return State(nlist=[note])


builder = StateGraph(State)
builder.add_node("a", node_a)
builder.add_edge(START, "a")
builder.add_edge("a", END)

graph = builder.compile()


# display(graph.get_graph().draw_mermaid_png())
print(graph.get_graph().draw_ascii())


inital_state = State(nlist=["hi there"])

print(graph.invoke(inital_state))

