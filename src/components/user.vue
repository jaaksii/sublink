<template>
<div>
  <div style="display: flex;justify-content: center">
  <span>{{username}}</span>
  <span style="margin-left: 10px">
    <el-button size="mini" @click="ifOutUser">注销</el-button>
  </span>
  </div>
  <div style="margin-bottom: 10px"></div>
  <el-input
    type="text"
    v-model="newUserName"
    placeholder="新账号"
  >
    <template slot="prepend">新账号</template>
  </el-input>
  <div style="margin-bottom: 10px"></div>
  <el-input
    type="text"
    v-model="password"
    placeholder="新密码"
    @keydown.enter.native="handleSetUser"
  >
    <template slot="prepend">新密码</template>
  </el-input>
  <div style="margin-bottom: 10px"></div>
  <el-button round style="position: relative;left: 50%;transform: translate(-50%)" @click="handleSetUser">修改</el-button>
</div>
</template>

<script>
import { SetUser } from '@/api/user'
export default {
  name: 'MyUser',
  data () {
    return {
      username: '',
      newUserName: '',
      password: '',
      timer: ''
    }
  },
  created () {
    this.handleUser()
  },
  methods: {
    handleUser () {
      const token = JSON.parse(localStorage.getItem('token'))
      if (token) {
        const payload = token.split('.')[1]
        const decoded = JSON.parse(atob(payload))
        this.username = decoded.sub
      }
    },
    handleSetUser () {
      if (!/^\w{4,12}$/.test(this.newUserName)) return alert('请输入4-12位数字母或者数字账号')
      if (!/^\w{4,32}$/.test(this.password)) return alert('请输入4-32位数字母或者数字密码')
      clearTimeout(this.timer)
      this.timer = setTimeout(async () => {
        const { code, msg } = await SetUser({
          username: this.username,
          newUserName: this.newUserName,
          password: this.password
        })
        this.$message({
          type: code === 200 ? 'success' : 'warning',
          message: msg
        })
        if (code === 200) {
          this.$message({
            message: '现在请重新登录'
          })
          this.handleOutUser()
        }
      }, 1000)
    },
    handleOutUser () { // 注销用户
      localStorage.removeItem('token')
      localStorage.removeItem('refresh')
      location.reload()
    },
    ifOutUser () {
      this.$confirm('此操作将注销重新登录, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        center: true
      }).then(() => {
        this.handleOutUser()
      }).catch(() => {

      })
    }
  }
}
</script>

<style scoped>

</style>
