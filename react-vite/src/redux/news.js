const GET_ALL_NEWS = '/news/GET_ALL_NEWS'
const GET_ONE_NEWS = '/news/GET_ONE_NEWS'

const getAllNews = news => {
    return {
        type: GET_ALL_NEWS,
        news
    }
}

const getOneNews = news => {
    return {
        type: GET_ONE_NEWS,
        news
    }
}

export const fetchAllNews = () => async (dispatch) => {
    const res = await fetch('/api/news/')

    if (res.ok) {
        const news = await res.json()
        dispatch(getAllNews(news))
        return news
    }
}

export const fetchNewsDetails = (newsId) => async (dispatch) => {
    const res = await fetch(`/api/news/${newsId}/`)

    if (res.ok) {
        const news = await res.json()
        dispatch(getOneNews(news))
        return news
    }
}

const initialState = {}
const newsReducer = (state=initialState, action) => {
    switch (action.type) {
        case GET_ALL_NEWS: {
            const newsState = { ...state }
            action.news.forEach(post => (newsState[post.id] = post))
            return newsState
        }
        case GET_ONE_NEWS: {
            return {
                ...state,
                [action.news.id]: action.news
            }
        }
        default:
            return state
    }
}

export default newsReducer