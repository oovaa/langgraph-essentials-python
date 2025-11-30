from langgraph.types import Command
from langgraph.graph.state import CompiledStateGraph
import operator
from typing import Annotated, List, Literal, TypedDict
from langgraph.graph import END, START, StateGraph


class State(TypedDict):
    nlist: Annotated[List[str], operator.add]


def node_a(state: State) -> Command[Literal["b", "c", END]]:
    select: str = state["nlist"][-1]
    if select == "b":
        next_node = "b"

    elif select == "c":
        next_node = "c"

    elif select == "q":
        next_node: str = END
    else:
        next_node = END

    return Command(update=State(nlist=[next_node]), goto=[next_node])


def node_b(state: State) -> State:
    return State(nlist=["B"])


def node_c(state: State) -> State:
    return State(nlist=["C"])


# def confitional_edge(state: State) -> Literal["b", "c", END]:
#     select: str = state["nlist"][-1]
#     if select == "b":
#         next_node = "b"

#     if select == "c":
#        next_node = "c"

#     if select == "q":
#         next_node = END
#     return Command(
#         update = State(nlist = [select]),
#         goto = next_node
#     )

builder = StateGraph(State)
builder.add_node("a", node_a)
builder.add_node("b", node_b)
builder.add_node("c", node_c)


builder.add_edge(START, "a")
builder.add_edge("b", END)
builder.add_edge("c", END)
# builder.add_conditional_edges("a", confitional_edge)


graph = builder.compile()
print(graph.get_graph().draw_ascii())


# png_data = graph.get_graph().draw_mermaid_png()
# with open("my_langgraph.png", "wb") as f:
# f.write(png_data)


user: str = input("b, c, or q")

input_state = State(nlist=[user])

print(graph.invoke(input_state))
