num_threads=32
for i in 2
do
  bash generate_for_deflection.sh ${i} ${num_threads} || exit 1
done
