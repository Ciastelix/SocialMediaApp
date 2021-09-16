import React, {useState} from 'react'
import axios from 'axios'
import styles from './Add.module.css'
export default function AddPost() {
    const [title, setTitle] = useState();
    const [content, setContent] = useState();
    const add = () => {
        axios.post("http://localhost:8000/api/add-post", {"title": title, "content": content}).then((res)=>console.log(res))
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