{{/*
Expand the name of the chart.
*/}}
{{- define "flask-app.fullname" -}}
{{- printf "%s-%s" .Chart.Name .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}