#este readme contendra a futuro informacion de el proyecto
"1. mv .env.example .env"
"2. Renombra el archivo .env.example a .env y ejecuta docker compose up -d"
"3. docker compose exec --user root checkmk bash -c "cp /omd/sites/cmk/share/check_mk/agents/plugins/mk_logwatch* /usr/lib/check_mk_agent/plugins/ && chmod +x /usr/lib/check_mk_agent/plugins/mk_logwatch* && mkdir -p /etc/check_mk && echo -e '/app/logs/honeypot_auth.log\n C ALERTA DE SEGURIDAD' > /etc/check_mk/logwatch.cfg && cp /omd/sites/cmk/share/check_mk/agents/plugins/mk_docker.py /usr/lib/check_mk_agent/plugins/ && chmod +x /usr/lib/check_mk_agent/plugins/mk_docker.py"
"4. Entrar en la página de Checkmk y añadir el host localhost"
