import React, {useState, useEffect} from 'react' 

function App(){

  const [data, setData] = useState([{}])

  useEffect(()=>{
    fetch("/database").then(
      res=> res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return(
    <div>
      {(typeof data.nombre === 'undefined') ? (
        <p>Loading...</p>
      ):(
        data.nombre.map((nom, i) => (
          <p key = {i}>{nom}</p>
        ))
      )}
    </div>
  )
}

export default App