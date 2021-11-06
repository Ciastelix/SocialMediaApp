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
                    </>
                }
            </> :
            <h1>Loading...</h1>}
        </>
    )
}
