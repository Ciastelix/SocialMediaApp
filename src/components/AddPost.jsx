import React, {useState} from 'react'
import axios from 'axios'
import styles from './Add.module.css'
import Cookies from 'universal-cookie';
import { useHistory } from 'react-router';
export default function AddPost() {
    let hist = useHistory();
    const [title, setTitle] = useState();
    const [content, setContent] = useState();
    const cookies = new Cookies();
    const success = () => {
        hist.push("/")
        window.location.reload()
    }
    const add = () => {
        const token = cookies.get('token')
        let headers = {
           'Content-Type' : 'application/json',
            'Accept' : 'application/json',
            'Authorization' : `Bearer ${token}`
        }
        axios.post("http://localhost:8000/posts", {"title": title, "content": content}, {headers: headers}).then((res)=>success()).catch((error)=>alert("Error"))
    }
    return (
        <form className={styles.Form}>
            <label className={styles.Label} for="_title_">
                title
            </label>
                <input className={styles.Input} type="text" name="_title" id="_title_" onClick={e => setTitle(e.target.value)} />
            
            <br />
            <label className={styles.Label} for="_lastName_">
                content
            </label>
            <input className={styles.Input} type="text" name="_content" id="_content_" onClick={e => setContent(e.target.value)} />
            <br />
            <input className={styles.Input} type="button" value="Add Post" onClick={add}/>
        </form>
    )
}