import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { useParams } from 'react-router-dom'
import styles from './Profile.module.css'

export default function Profile() {
    const [userData, setUserData] = useState(undefined);
    const [posts, setPosts] = useState(undefined)
    const { id } = useParams();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get(`http://localhost:8000/users/me`).then((res) => setUserData(res.data))
        setLoading(false)
    }, [id])
    return (
        <>
            {!loading ? <>
                {userData && posts && <><h1 className={styles.Header}>Profile of {`${userData.firstName} ${userData.lastName}`}</h1>
                    <div className={styles.PostsPage}>
                    <h2 className={styles.Content}>Posts</h2>
                    {userData.posts.map((post) => (<><h3 className={styles.PostTitle}>{post.title}</h3><p className={styles.PostContent}>{ post.content }</p></>))}
                    </div>
                    </>
                }
            </> :
            <h1>Loading...</h1>}
        </>
    )
}

