const NEWS_TOPICS = 'Linux OR Open-Source OR Android'
const NEWS_LANGS = 'en'
const API_KEY = '07867c2e083c43c69201be599ab7ddd9'

fetch(`https://newsapi.org/v2/everything?q=${NEWS_TOPICS}&apiKey=${API_KEY}&language=${NEWS_LANGS}`)
    .then((response) => {
        return response.json();
    })
    .then((myJson) => {
        const articles = myJson['articles'];
        console.log(articles);
        for (let i = 0; i < articles.length; ++i) {
            const article_box = document.getElementById(i);

            const title_div = document.createElement('div')
            title_div.className = 'grid-item-title'
            const title = document.createElement('h2');
            const node = document.createTextNode(articles[i]['title']);
            title.appendChild(node)
            title_div.appendChild(title)
            article_box.appendChild(title_div);

            const image_div = document.createElement('div')
            image_div.className = 'grid-item-img'
            const image = document.createElement('img')
            image.src = articles[i]['urlToImage'];
            image_div.appendChild(image);
            article_box.appendChild(image_div);

            

            const description_div = document.createElement('div');
            description_div.className = 'grid-item-desc';
            const description = document.createElement('p');
            const desc_node = document.createTextNode(articles[i]['description']);
            description.appendChild(desc_node);
            description_div.appendChild(description);
            article_box.appendChild(description_div);

            const click_div = document.createElement('div');
            click_div.className = 'grid-item-click';
            const click = document.createElement('a');
            click.href = articles[i]['url'];
            const click_node = document.createTextNode('Read More >>>');
            click.appendChild(click_node);
            click_div.appendChild(click);
            article_box.appendChild(click_div);
        }
    })