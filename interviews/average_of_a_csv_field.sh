#
# Given a csv file and a field number, display the average for that field.
#
file=$1
field=$2

counter=0
total=0
while read -r line
do
    total=$(( $total + `echo $line | cut -d "," -f$field`))
    counter=$(( $counter + 1))
done <<< `tail $file -n +2`

average=$(( $total / $counter ))
echo Average for field No $field is $average
