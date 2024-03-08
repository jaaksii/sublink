<template>
<div>
  <el-button @click="clash_config('edit')"> 编辑规则</el-button>
  <el-tag style="margin-left: 10px" size="mini" type="info">适配:ss vmess trojan hy2</el-tag>
  <el-dialog
    title="surge规则编辑(所有订阅共用一个规则)"
    :visible.sync="dialogVisible"
    width="80%"
  >
    <span>建议复制出来修改后在替换上去，这里修改内容会有卡顿</span>
    <p>[Proxy Group]下里面写上auto会插入本订阅所有节点名称列表</p>
    <div style="margin-bottom: 10px"></div>
    <span>
      <el-input
        v-model.lazy="config"
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
import { GetSurge } from '@/api/nodetype'
export default {
  name: 'MySurge',
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
        const { code, msg } = await GetSurge({
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
        const { code, msg } = await GetSurge({
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
