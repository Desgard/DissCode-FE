<template>
  <panel class="container">
    <div slot="title">{title}</div>
  </panel>
</template>

<script>

export default {
  name: 'ShowCardView',
  props: {
    title: String
  }
}
</script>

<style scoped lang="less">
  .container {
    margin-bottom: 20px;

    .content {
      font-size: 16px;
      margin: 0 50px 20px 50px;
      > ul {
        list-style: disc;
        li {
          line-height: 2;
          .title {
            font-weight: 500;
          }
        }
      }
    }
  }
</style>