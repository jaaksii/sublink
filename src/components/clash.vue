<template>
<div>
  <el-button @click="clash_config('edit')">编辑规则</el-button>
  <el-dialog
    title="clash规则编辑"
    :visible.sync="dialogVisible"
    width="80%"
  >
    <span>
      <el-input
        v-model="config"
        type="textarea"
        rows="10"
      ></el-input>
    </span>
    <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="clash_config('save')">保 存</el-button>
  </span>
  </el-dialog>
</div>
</template>

<script>
import { GetClash } from '@/api/clash'
export default {
  name: 'MyClash',
  data () {
    return {
      dialogVisible: false,
      config: ''
    }
  },
  created () {

  },
  methods: {
    async clash_config (index) {
      // console.log(index)
      if (index === 'edit') {
        const { code, msg } = await GetClash({
          index: 'read'
        })
        this.dialogVisible = true
        if (code === 200) {
          this.config = msg
        } else {
          this.$message({
            type: 'warning',
            message: '读取不到，错误'
          })
        }
      }
      if (index === 'save') {
        // console.log('sava')
        const { code, msg } = await GetClash({
          index: 'save',
          text: this.config
        })
        if (code === 200) {
          this.$message({
            type: 'success',
            message: '保存成功'
          })
          // console.log('保存成功')
        } else {
          this.$message({
            type: 'warning',
            message: msg
          })
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
