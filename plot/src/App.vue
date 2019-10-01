<template>
  <div id="app" class="app">
    <b-upload class="upload" v-model="file" multiple drag-drop>
      <span class="upload-icon">+</span>
    </b-upload>

    <b-dropdown  class="mode" aria-role="list" v-model="mode">
        <p
            class="tag is-success"
            slot="trigger"
            role="button">
            {{mode}}
        </p>

        <b-dropdown-item value="BoxPlot" aria-role="listitem">BoxPlot</b-dropdown-item>
        <b-dropdown-item value="Histogram" aria-role="listitem">Histogram</b-dropdown-item>
    </b-dropdown>

    <div class="plot">
      <div id="boxplot">

      </div>
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js'

export default {
  name: "app",
  data() {
    return {
      file: null,
      fileContent: null,
      data: [],
      mode: 'BoxPlot'
    };
  },
  methods: {
    addBoxPlot(content, fileName) {
      let lines = content.split("\n");
      let y0 = lines.map(d => parseInt(d.split("\t").slice(-2)[0]));
      y0 = y0.filter(d => Number.isInteger(d));

      var trace1 = {
        y: y0,
        type: "box",
        name: fileName
      };

      this.data.push(trace1)
      this.$nextTick(() => {
        Plotly.newPlot("boxplot", this.data);
      });
    },
    addHistogram(content, fileName) {
      let lines = content.split("\n");
      let y0 = lines.map(d => parseInt(d.split("\t").slice(-2)[0]));
      y0 = y0.filter(d => Number.isInteger(d));

      var trace1 = {
        x: y0,
        type: "histogram",
        name: fileName
      };

      this.data.push(trace1)
      this.$nextTick(() => {
        Plotly.newPlot("boxplot", this.data);
      });
    },
    plot() {
      this.file.forEach(file => {
        this.data = []
        var reader = new FileReader();
        reader.readAsText(file, "UTF-8");
        if (this.mode == 'BoxPlot') {
          reader.onload = evt => this.addBoxPlot(evt.target.result, file.name);
        } else {
          reader.onload = evt => this.addHistogram(evt.target.result, file.name);
        }
      });
    }
  },
  watch: {
    file: function() {
      this.plot()
    },
    mode: function() {
      this.plot()
    }
  }
};
</script>

<style lang="scss" scoped>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: relative;
  background-color: #eee;
  height: 100vh;
  width: 100vw;
}

.upload {
  position: absolute;
  display: block;
  top: 10px;
  left: 10px;
  width: 50px;
  text-align: center;
  z-index: 999;

  &-icon {
    width: 100%;
    height: 100%;
    font-size: 2rem;
  }
}

.mode {
  display: block;
  position: absolute;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 999;
}

.plot {
  height: 90vh;
  margin-top: 30px;
  width: 90vw;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 10px;
  padding: 20px;
  background-color: #fff;
}
</style>