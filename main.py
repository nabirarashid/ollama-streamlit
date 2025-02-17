import streamlit as st
import ollama

# initialize conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation =[]
    
st.header("Welcome to Ollama! :3")
st.subheader("Chat with the Llama Model")

word = st.text_input("What would you like to say? ")

if st.button("Send"):
    if word:
        # add to conversation history
        st.session_state.conversation.append({"role": "user", "content": word})

        # getting a response
        try:
            stream = ollama.chat(
                model = "llama2",
                messages = [{"role": "user", "content": word}],
                stream = True,
                )

            full_message = ""
            for chunk in stream:
                full_message += chunk["message"]["content"] + " "

            # add response to conversation history
            st.session_state.conversation.append({"role": "llama", "content": full_message})
        
        except Exception as e:
            st.error(f"An error occurred: {e}")

# displaying the conversation history
for message in st.session_state.conversation:
    if message["role"] == "user":
        st.write(f"You: {message['content']}")
    else:
        st.write(f"Llama: {message['content']}")
