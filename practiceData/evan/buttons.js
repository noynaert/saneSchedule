const app = Vue.createApp({
  methods: {},
  data: function () {
    return {
      disciplineName: "None Picked",

      disciplines: [
          { disc: "CSC", disciplineName: "Computer Science" },
          { disc: "MAT", disciplineName: "Mathematics"},
          { disc: "HON", disciplineName: "Honors"}
    ],
    
    };
  },
});
app.mount("#pickDisc");
