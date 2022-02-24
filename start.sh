if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/LordSA/movie-world.git /movie-world
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /movie-world
fi
cd /movie-world
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
