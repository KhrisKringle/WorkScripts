#!/bin/zsh


if [ -z "$1" ]; then
	read input_string
	schoolname="$input_string"
else
	schoolname="$1"
	cd ~"/Downloads/"
fi

cd ~"/Downloads/"
# Check if the files exist
if [[ -f TeacherCertification_ALL.csv && -f StudentSeatTime_ALL.csv && -f StudentSeatTime_MONTH.csv ]]; then
    # Create the directory if it doesn't exist
    mkdir -p Acellus\ Reports

    # Move the files into the directory
    mv TeacherCertification_ALL.csv StudentSeatTime_ALL.csv StudentSeatTime_MONTH.csv Acellus\ Reports
    echo "Files moved successfully."
	#Makes the Managed Schools Dowloaded data if it doesn't exist
	mkdir -p ~"/Documents/Managed Schools Downloaded data"

	mv Acellus\ Reports $schoolname
	mv -f $schoolname ~"/Documents/Managed Schools Downloaded data"

	python3 ~"/Downloads/chrisstats/Report_Card.py" ~"/Documents/Managed Schools Downloaded data/$schoolname"
else
    echo "One or more files are missing."
fi