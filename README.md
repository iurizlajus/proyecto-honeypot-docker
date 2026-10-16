#este readme contiene informacion de como desplegar correctamente el proyecto
"1. primero compiaremos el .env.example a un .env para que 
	cp .env.example .env"

"2. docker compose up -d"

"3. Para obtener acceso al cmk revisar la contraseña proporcionada en los logs despues de el compose 
    docker logs checkmk_monitor | grep -i password"

"4. ¡¡¡ESPERAR 2 MINUTOS PARA QUE A CMK LE DE TIEMPO A MONTARSE YA QUE SI NO DARA LUGAR A ERRORES Y RUTAS CORRUPTAS!!"

"5. Instalar los plugins para que CMK pueda vigilar los contenedores y el log de la web con los logwatchs
	docker compose exec --user root checkmk bash -c "cp /omd/sites/cmk/share/check_mk/agents/plugins/mk_logwatch* /usr/lib/check_mk_agent/plugins/ && chmod +x /usr/lib/check_mk_agent/plugins/mk_logwatch* && mkdir -p /etc/check_mk && echo -e '/app/logs/honeypot_auth.log\n C ALERTA DE SEGURIDAD' > /etc/check_mk/logwatch.cfg && cp /omd/sites/cmk/share/check_mk/agents/plugins/mk_docker.py /usr/lib/check_mk_agent/plugins/ && chmod +x /usr/lib/check_mk_agent/plugins/mk_docker.py"

"6. Entrar en la página de Checkmk y añadir el host localhost"
