const input = document.querySelector('#todo-input')
const inputBtn = document.querySelector('#input-btn')
const todoList = document.querySelector('ul')

const addTodo = event => {
  event.preventDefault()

  const content = input.value

  if (content.trim()) {
    const todo = document.createElement('li')
    todo.innerHTML = content

    const delBtn = document.createElement('button')
    delBtn.innerText = 'X'
    delBtn.setAttribute('class', 'delbtn')

    todo.appendChild(delBtn)
    todoList.appendChild(todo)

    const remove = event => {
      event.preventDefault()
      todoList.removeChild(todo)
    }

    const done = event => {
      event.preventDefault()
      todo.classList.toggle('done')
    }

    delBtn.addEventListener('click', remove)
    todo.addEventListener('click', done)

  } else {
    alert ('You must Input Todo-things')
  }
  input.value = null
}

inputBtn.addEventListener('click', addTodo)