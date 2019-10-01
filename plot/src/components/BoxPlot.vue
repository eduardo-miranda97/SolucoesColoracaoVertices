<template>
  <div id="boxplot">
  </div>
</template>

<script>
import Plotly from 'plotly.js'

export default {
  props: ['data'],
  
  created() {
    let lines = this.data.split('\n')
    let y0 = lines.map((d) => parseInt(d.split('\t').slice(-2)[0]))
    y0 = y0.filter((d) => Number.isInteger(d))

    var trace1 = {
      y: y0,
      type: 'box'
    };

    var data = [trace1]
    this.$nextTick(() => {
      Plotly.newPlot('boxplot', data);
    })
  }
}
</script>

<style>

</style>