if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/LordSA/movie-world.git /MovieWorld
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MovieWorld
fi
cd /MovieWorld
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
