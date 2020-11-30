
const app = Vue.createApp({
    created: function(){
        console.log("in created")
    },
    data(){
        return{
            discSelect:"",
            discName:"",
            pickBy:"",
            // disciplines:{
            //   BIO:"Biology",
            //   ACT:"Applied Computer Technology",
            //   CSC:"Computer Science",
            //   MAT:"Mathematics",
            //   PHY:"Physics"
            // }
            discStatus: "Not Loaded",
            disciplines: new Array()   
        }
    },
    methods:{
        
        changeDisc(){
            console.log("discSelect is "+this.discSelect);
        
            this.pickBy = "Discipline";
      }
    },
    mounted: function () {
        console.log("Mounted");
    
        this.discStatus = "Loading..."
        //   .get('https://api.coindesk.com/v1/bpi/currentprice.json')
       fetch('./discFile.json')
          .then( response =>{
              console.log(response);
              if(response.ok){
                  console.log("Response is OK");
                  return response.json();
              }
          }).then( data=> {
              console.log("Got the data: "+(data));
              for(const disc in data){
                  //this.disciplines[disc] = data[disc];
                  //console.log(this.disciplines['disc])
                  var d = {};
                  d.abbr=disc;
                  d.full=data[disc];
                  this.disciplines.push(d);                  
                  console.log(d);
                  
              }
              this.discStatus = "Disciplines Loaded.";
              
          })
      }
});

app.mount("#saneSched");