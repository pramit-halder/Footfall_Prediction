import footfall1 from './footfall2.jpg'
import footfall2 from './footfall1.jpg'
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { Component } from 'react';
import axios from 'axios';
import loaderGIF from './plane.gif';
import logo1 from './mllogo.png';


class App extends Component {
  constructor(props) {

    super(props);
    this.state = {
      data1: "",
      data2: "",
      data3: "",
      data: "",
      loading: false,
    };
    this.formRef = React.createRef();
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    this.setState({ loading: true })
    console.log("handleSubmit called");
    // here my flask is running it localhost
    // axios.post('http://localhost:5000/model1', { x: this.state.data })
    //   .then((response1) => {
    //     this.setState({ data1: response1.data })
    //     console.log(response1.data)
    //   })
    // axios.post('http://localhost:5000/model2', { x: this.state.data}).then((response2) => {
    //   this.setState({ data2: response2.data })
    //   console.log(response2.data)
    // })
    // axios.post('http://localhost:5000/model3', { x: this.state.data}).then((response3) => {
    //   this.setState({ data3: response3.data })
    //   console.log(response3.data)
    // })
    axios.all([
      axios.post('http://localhost:5000/model1', { x: this.state.data }),
      axios.post('http://localhost:5000/model2', { x: this.state.data }),
      axios.post('http://localhost:5000/model3', { x: this.state.data })
    ])
      .then(res => {
        this.setState({ data1: res[0].data, data2: res[1].data, data3: res[2].data })
        this.setState({ loading: false })
         console.log(res[0].data);
         console.log(res[1].data);
         console.log(res[2].data);
      })
  }


  // show(e){

  //   let image = document.getElementById("images").style.display="block";
  //   document.getElementById("btnid").style.display="none";

  // }

  render() {
    const { data1, data2, data3 } = this.state;
    console.log(this.state)
    return (
   <div>

    <div className='apps'> 
        <div className='header'>
      {/* heading */}
      <img src={logo1} style={{textAlign:'left', width:'50px',height:'50px',marginbottom:'10cm'}}></img>
      <h1><b>ML WIZARDS</b></h1>
      
      {/* heading ends */}
      </div>
    {/* this is for footfall prediction navbar */}
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#">TRENDS</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
   <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
      <a class="nav-item nav-link active" href={footfall1}>Yearwise Footfall</a>
      <a class="nav-item nav-link" href={footfall2}>Overall Footfall</a>
    </div>
  </div>
</nav>
{/* navbar ends */}

{/* form starts */}
<form ref={this.formRef} method='POST' onSubmit={this.handleSubmit}>
  {/* input starts */}
<div className="inputs">
<h3>Click here for prediction :</h3>
<br></br>
<label for="bfj"> 
  <input type="radio"  id="before" name="Date" value = "1" style={{ width: '24px', height: '24px',display: 'flex',
  }} onChange={
    (e) => {
      console.log("hello")
      this.setState({ data: e.target.value })
      console.log("data")
    }
  }/><b style={{verticalAlign:'baseline'}}>Before 4th of july</b>
</label>
<br></br>
<label for="afj">
<input type="radio"  id="after" name="Date" value = "2" 
  style={{ width: '24px', 
          height: '24px',
          display: 'flex',
          verticalAlign:'baseline'
           }}
  onChange={(e) => {
      console.log("hello")
      this.setState({ data: e.target.value })
      console.log("data")
    }
  } /><b>After 4th of july</b>
</label>
<br></br>
<label for="range">
<input type="radio"  id="range" name="Date" value = "3"
style={{ width: '24px',
         height: '24px',
         display: 'flex',
          }}
onChange={(e) => {
    console.log("hello")
    this.setState({ data: e.target.value })
    console.log("data")
    }
  } /><b>Between 15th Feb to 5th Mar</b>
</label>

<br></br>
{/* input ends */}

{/* submission starts */}

<button type="button" onClick={this.handleSubmit}>Submit</button>
{this.state.loading === true ?
            <img src={loaderGIF} height={"200px"} />
            : <div className='datass'>
              <p>{data1}</p>
              <p>{data2}</p>
              <p>{data3}</p>
            </div>
          }
</div>
{/* submission ends */}
</form>
{/* form ends */}
        </div>
        <div id="output">gjrgiueggij
          {this.state.loading === true ?
            <img src={loaderGIF} height={"200px"} />
            : <div className='datass'>
              <p>{data1}</p>
              <p>{data2}</p>
              <p>{data3}</p>
            </div>
          }       </div>
       
       </div>
    );

  }
}
export default App;
