import { Route, Switch, Link } from 'react-router-dom';
import './App.css';
import AddPost from './components/AddPost';
import Profile from './components/Profile';
import AddUser from './components/AddUser';
import NavBar from './components/NavBar';
import SearchForUser from './components/SearchForUser'
import { createContext, useState, useEffect } from 'react';
import axios from 'axios';
export const MainContext = createContext();
function App() {
  const [usrname, setUsrname] = useState(undefined);
  const [posts, setPosts] = useState([]);
  const currUsername = {
    usrname: usrname,
    setUsrname : (usr) => setUsrname(usr)
  }
      useEffect(() => {
        axios.get(`http://localhost:8000/get/posts`).then((res) => setPosts(res.data))
      }, [])
  return (
    <MainContext.Provider value={currUsername}>
    <div className="App"> 
        <NavBar />
        
      <Switch>
        
        <Route exact path="/" />
        <Route path="/profile/:id" component={Profile} />
        <Route path="/add/post" exact component={AddPost} />
        <Route path="/add/user" exact component={AddUser} />
        <Route path="/search/user/:usr" exact>
          <SearchForUser/>
        </Route>


        </Switch>
        {posts.map((post => (
          <>
            <h1>{post.title}</h1>
            <p>{post.content}</p>
          </>
        )
        ))}
      </div>
      </MainContext.Provider>
  );
}

export default App;
