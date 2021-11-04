const app = new Vue ({
  el: '#app',
  data: {
    todoList: [],
    input: '',
    status: 'all',
  },
  methods: {
    addTodo: function () {
      if (this.input.length > 0) {
        this.todoList.push({
          isComplete: false,
          content: this.input,
          key: Date.now()
        })
      } else {
        alert ('※ 내용을 입력하세요 ※')
      }
      this.input = ''
    },

    removeComplete: function () {
      this.todoList = this.todoList.filter(todo => !todo.isComplete)
    },

    save: function () {
      localStorage.setItem('todoList', JSON.stringify(this.todoList))
    },

    load: function () {
      const loadData = JSON.parse(localStorage.getItem('todoList'))
      this.todoList = loadData || []
    },

    reset: function () {
      this.todoList = []
    }
  },
  computed: {
    todoListStatus: function () {
      const tempList = this.todoList.filter(todo => {
        if (this.status === 'complete') {
          return todo.isComplete
        } else if (this.status === 'progress') {
          return !todo.isComplete
        } else {
          return true
        }
      })
      return tempList
    }
  },
  watch: {
    todoList: {
      handler: function() {
        this.save()
      },
      deep: true
    }
  },
  created: function () {
    this.load()
  }
})