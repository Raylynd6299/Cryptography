import React, { Component } from 'react';

class About extends Component {
  render() {

    if(this.props.data){
      var name = this.props.data.name;
      var profilepic= "images/"+this.props.data.image;
      var bio = this.props.data.bio;
      var street = this.props.data.address.street;
      var city = this.props.data.address.city;
      var state = this.props.data.address.state;
      var zip = this.props.data.address.zip;
      var phone= this.props.data.phone;
      var email = this.props.data.email;
      var resumeDownload = this.props.data.resumedownload;
      var publicKey = this.props.data.publicKey;
    }

    return (
      <section id="about">
      <div className="row">
         <div className="three columns">
            <img className="profile-pic"  src={profilepic} alt="Ray Profile Pic" />
         </div>
         <div className="nine columns main-col">
            <h2>Sobre mí</h2>

            <p>{bio}</p>
            <div className="row">
               <div className="columns contact-details">
                  <h2>Contacto</h2>
                  <p className="address">
						   <span>{name}</span><br />
						   
                     <span>{email}</span>
					   </p>
               </div>
               <div className="columns download">
                  <p>
                     <a href={resumeDownload} download="CV-RaymmundoPB.pdf"className="button"><i className="fa fa-download"></i>Download CV</a>
                     <a href={publicKey} className="button"><i className="fa fa-download"></i>Llave Publica</a>
                  </p>
               </div>
            </div>
         </div>
         <div className="nine columns main-col">
            <h2>Formación Academica</h2>
            <p>
               En cuanto a mi formacion academica profesional, la estoy cursando en IPN-ESCOM, en la Escuela Superior de Computo se generan los mejores ingenieros de computo en méxico
               por lo que estoy feliz de decir que actualmente cuento con un promedio 9.17 al Diciembre del 2020
            </p>
         </div>
         <div className="twelve columns main-col">
            <h2>Hobbies</h2>
            <ul>
               <li>Leer <a href="https://www.youtube.com/watch?v=R0zorGrtEBs">Ver aqui</a></li>
               <li>Jugar Basketball <a href="https://www.youtube.com/watch?v=8jqNmolWE9A">Ver aqui</a></li>
               <li>Programar <a href="https://www.youtube.com/watch?v=X5Wkp1gsNik&t=10s">Ver aqui</a></li>
            </ul>
         </div>
         <div className="twelve columns main-col">
            <h2>Acerca de Criptografía</h2>
            <p>
               Alan Turing fue un brillante matemático, criptoanalista e informático teórico nacido el veintitrés de Junio de 1912 en Maida Vale un distrito residencial al oeste de Londres. Turing, ademas de ser un brillante científico era homosexual, lo cual le costó la vida el siete de junio de 1954.
               <br/>
               Turing es mundialmente conocido por cuatro hechos:
            </p>
            <ul>
               <li>Formalizó los conceptos de algoritmo y computación con su máquina de Turing</li>
               <li>Es considerado el padre de la inteligencia artificial</li>
               <li>Su participación en el equipo de criptoanálisis de la máquina de criptografía alemana Enigma fue clave</li>
               <li>Fue una víctima más de la mentalidad reaccionaria puritana del mundo anglosajon</li>
            </ul>
         </div>
         
      </div>

   </section>
    );
  }
}

export default About;
