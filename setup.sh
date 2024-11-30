mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#f188be'\n\
backgroundColor = '#48933a'\n\
secondaryBackgroundColor = '#ede4d6'\n\
textColor = '#fff'\n\
" > ~/.streamlit/config.toml