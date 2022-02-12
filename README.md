<h1 align="left">
    <a href="https://github.com/m4mallu">Pdf Compressor Telegram Bot
</a>
</h1>

#### A simple pdf size compressing telegram robot. Useful for digital documentation.

<details>
  <summary><b>Mandatory Variables</b></summary>
    <p align="left">

    API_HASH    -   Your API Hash from my.telegram.org
    APP_ID      -   Your APP ID from my.telegram.org
    BOT_TOKEN   -   Your bot token from @BotFather
</p>
</details>
<details>
    <summary><b>Deploy</b></summary>
    <p align="left"></p>
        <b><u>Deploy in VPS:</u></b>
        <ul>
            <li><strong>Open a Linux Terminal and Run the below commands ( Stage: 1 )</strong></li>
            <li><code>git clone https://github.com/m4mallu/compress-pdf-tg-bot</code></li>
            <li><code>cd compress-pdf-tg-bot</code></li>
            <li>Create a <code>config.py</code> with the Mandatory variables (Refer sample_config.py) and save it in the bot directory.</li>
            <li><strong>Run the below commands in the same terminal ( Stage: 2 )</strong></li>
            <li><code>virtualenv -p python3 venv</code></li>
            <li><code>. ./venv/bin/activate</code></li>
            <li><code>pip3 install -r requirements.txt</code></li>
            <li><code>python3 bot.py</code></li>
        </ul>
        <b><u>Deploy in Heroku</u></b>
        <ul>
            <li><strong>Click the below button to deploy the bot in Heroku</strong></li>
            <a href="https://heroku.com/deploy?template=Your_Repo">
            <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
        </a>
        </ul>
</details>
<details>
  <summary><b>License</b></summary>
    <p align="left">
    <a href="https://choosealicense.com/licenses/gpl-3.0/">
        <img src="https://img.shields.io/badge/License-GPLv3-blueviolet?style=for-the-badge&logo=gplv3">
    </a>
</p>      
</details>
<details>
  <summary><b>Credits</b></summary>
    <p align="left">
      <a href="https://github.com/pyrogram/pyrogram">
        <img src="https://img.shields.io/badge/Pyrogram-MTProto%20API-orange?style=for-the-badge&logo=pyrogram" height="32.8">
    </a><br>
    <a href="https://github.com/SpEcHiDe">
        <img src="https://img.shields.io/badge/-SpEcHiDe-orange" height="30">
    </a>
    <a href="https://www.thepythoncode.com/article/compress-pdf-files-in-python">
        <img src="https://img.shields.io/badge/-PDFNetPython3-orange" height="30">
    </a>
</p>
</details>

