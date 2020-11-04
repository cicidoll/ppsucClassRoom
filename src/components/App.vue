<template>

  <div id="app" v-cloak>
    <div id="banner">

    </div>

    <div id="body-content">
      <tabs v-model="activeKey">
        <pane label="标签一" name="1">
          标签一的内容
        </pane>
        <pane label="标签二" name="2">
          标签二的内容
        </pane>
        <pane label="标签三" name="3">
          标签三的内容
        </pane>
        <pane label="标签四" name="4">
          标签四的内容
        </pane>
        <pane label="标签五" name="5">
          标签五的内容
        </pane>
      </tabs>
    </div>
  </div>

</template>

<script>
import pane from './Pane.vue'
import tabs from './Tabs.vue'

export default {
  data: function () {
    return {activeKey: '1'}
  },
  components: {
    pane,
    tabs
  }
}
</script>
