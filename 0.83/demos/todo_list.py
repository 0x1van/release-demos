import streamlit as st


def todo_list():
    st.write(
        """
        # ✅ Todo List
        
        This app stores a list of todo items in `st.session_state`. Additionally, it 
        uses the new `on_change` callback to add a new item only when the value of the 
        text field below changed.
        """
    )

    # Define initial state.
    if "todos" not in st.session_state:
        st.session_state.todos = [
            {"description": "Try out this TODO app", "done": True},
            {"description": "Play some Tic Tac Toe", "done": False},
            {"description": "Read the blog post about session state", "done": False},
        ]

    # Define callback when text_input changed.
    def new_todo_changed():
        if st.session_state.new_todo:
            st.session_state.todos.append(
                {
                    "description": st.session_state.new_todo,
                    "done": False,
                }
            )

    # Show widgets to add new TODO.
    st.write(
        "<style>.main * div.row-widget.stRadio > div{flex-direction:row;}</style>",
        unsafe_allow_html=True,
    )
    st.text_input("What do you need to do?", on_change=new_todo_changed, key="new_todo")

    # Show all TODOs.
    write_todo_list(st.session_state.todos)


def write_todo_list(todos):
    "Display the todo list (mostly layout stuff, no state)."
    st.write("")
    col1, col2 = st.beta_columns([0.1, 0.9])
    col1.write("*Done?*")
    col2.write("*Description*")
    for i, todo in enumerate(todos):
        done = col1.checkbox("", todo["done"], key=str(i))
        if done:
            format_str = (
                '<span style="color: grey; text-decoration: line-through;">{}</span>'
            )
        else:
            format_str = "{}"
        col2.markdown(
            format_str.format(todo["description"]),
            unsafe_allow_html=True,
        )