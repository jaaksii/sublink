<template>
<div>
  <el-tag style="margin-right: 10px">生成类型</el-tag>
  <el-select :value="obj.value" placeholder="生成类型" @change="handleValue">
    <el-option
      v-for="(item,index) in obj.option"
      :key="index"
      :value="item"
    >
    </el-option>
  </el-select>
</div>
</template>

<script>
export default {
  name: 'MyType',
  data () {
    return {
      value: '',
      option: ['v2ray', 'clash']
    }
  },
  props: {
    obj: Object
  },
  methods: {
    handleValue () {
      console.log('原' + this.value)
      this.$emit('handleValue', this.value)
    }
  }
}
</script>

<style scoped>

</style>
