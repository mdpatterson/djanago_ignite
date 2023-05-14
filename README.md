# djanago_ignite

#https://www.gridgain.com/docs/latest/installation-guide/installing-on-zos

  pip install -r requirements.txt

  sudo apt install apache-ignite --no-install-recommends
  
  export IGNITE_HOME=/usr/share/apache-ignite

  cp $IGNITE_HOME/libs/optional/ignite-rest-http $IGNITE_HOME/libs/ignite-rest-http
  
  mkdir /tmp/apache-ignite
  
  sudo ln -s /tmp/apache-ignite  $IGNITE_HOME/work
  
  nohup bash $IGNITE_HOME/bin/ignite.sh -v $IGNITE_HOME/config/default-config.xml 1> log.txt 2>&1 &
  
  cd djanago_ignite/tutorial
  
  http POST http://127.0.0.1:8000/snippets/ code='option1'
  
  http POST http://127.0.0.1:8000/snippets/ code='option2'
  
  http POST http://127.0.0.1:8000/snippets/ code='option3'


