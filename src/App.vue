<template>
  <div id="app">
    <router-view/>
    <div class="footer">
    <span>ver:{{ver}}</span>
    </div>
  </div>
</template>

<style lang="less">
//ver: process.env.VUE_APP_VER

#app{
  padding:0;
  margin:0;
}
.footer{
  position: absolute;
  left: 50%;
  bottom: 1%;
  transform: translate(-50%,-1%);
}
</style>
<script>
export default {
  data () {
    return {
      ver: process.env.VUE_APP_VER
    }
  }

}

</script>
