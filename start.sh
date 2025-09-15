if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/LordSA/Eren-Yeager-ADV5.2.0.git /Eren-Yeager-ADV5.2.0
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Eren-Yeager-ADV5.2.0
fi
cd /movie-world
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
