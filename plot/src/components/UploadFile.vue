<template>
  <b-upload v-model="file" drag-drop>
    <section class="section">
      <div class="content has-text-centered">
        <p>
          <b-icon icon="upload" size="is-large"></b-icon>
        </p>
        <p>Drop your files here or click to upload</p>
      </div>
    </section>
  </b-upload>
</template>

<script>
export default {
  data() {
    return {
      file: null,
      fileContent: null
    }
  },
  methods: {
    content() {
      
    }
  },
  watch: {
    file: function () {
      if (this.file != null) {
        var reader = new FileReader();
        reader.readAsText(this.file, "UTF-8")
        reader.onload = ((evt) => this.$emit('fileLoad', evt.target.result))
      }
    }
  }
};
</script>

<style>
</style>