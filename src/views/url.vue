<template>
<div>
{{text}}
</div>
</template>

<script>
import { GetSubName } from '@/api/sub'
export default {
  name: 'MyUrl',
  data () {
    return {
      text: ''
    }
  },
  created () {
    this.get_sub(this.$route.params.name)
    // console.log(this.$route.params.name)
  },
  methods: {
    async get_sub (name) {
      const { code, msg } = await GetSubName(name)
      if (code === 200) {
        this.text = msg
      }
      this.text = msg
    }
  }
}
</script>

<style scoped>

</style>
