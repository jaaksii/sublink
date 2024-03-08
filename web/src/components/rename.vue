<template>
<div>
  <el-button
    type="success"
    size="mini"
    style="margin-left: 10px"
    @click="handleOpen"
    round
  >修改订阅名称
  </el-button>
  <el-button
    type="danger"
    size="mini"
    style="margin-left: 10px"
    @click="handleDel"
    round
  >删除订阅
  </el-button>
  <el-dialog
    title="新订阅名称"
    :visible.sync="dialogVisible"
    >
    <el-input
      v-model.trim="rename"
      ref="inp"
      @keyup.enter.native="handleRename"
    />
    <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="handleRename">确 定</el-button>
  </span>
  </el-dialog>
</div>
</template>

<script>
export default {
  name: 'ReName',
  data () {
    return {
      dialogVisible: false,
      rename: ''
    }
  },
  methods: {
    handleOpen () {
      this.dialogVisible = true
      this.$nextTick(() => {
        // console.log(this.$refs.inp)
        this.$refs.inp.focus()
      })
    },
    handleRename () {
      this.$emit('handleRename', this.rename)
      this.dialogVisible = false
      this.rename = ''
    },
    handleDel () {
      this.$emit('handleDel')
    }
  }
}
</script>

<style scoped>

</style>
