#!/bin/bash


function scenario1 { 
    # No locks by offset
    echo "Scenario 1"
    echo "----------"
    python pocs/locks/fasteners_1.py -r ${1} & \
    python pocs/locks/fasteners_1.py -r ${1} & \
    python pocs/locks/fasteners_1.py -r ${1}
}

function scenario2 { 
    # All the locks on the same offset
    # No mixed offsets
    echo "Scenario 2"
    echo "----------"
    python pocs/locks/fasteners_1.py --offset 1 -r ${1} & \
    python pocs/locks/fasteners_1.py --offset 1 -r ${1} & \
    python pocs/locks/fasteners_1.py --offset 1 -r ${1}
}

function scenario3 { 
    # All the locks on the same offset
    # Mixed offsets
    echo "Scenario 3"
    echo "----------"
    python pocs/locks/fasteners_1.py --offset 1 -r ${1} & \
    python pocs/locks/fasteners_1.py --offset 2 -r ${1} & \
    python pocs/locks/fasteners_1.py --offset 1 -r ${1}
}

function scenario4 { 
    # Locks mixed between lock files and offsets
    # No mixed offsets
    echo "Scenario 4"
    echo "----------"
    python pocs/locks/fasteners_1.py --offset 1 -r ${1} & \
    python pocs/locks/fasteners_1.py -r ${1} & \
    python pocs/locks/fasteners_1.py --offset 1 -r ${1}
}

function scenario5 { 
    # Locks mixed between lock files and offsets
    # No mixed offsets
    echo "Scenario 4"
    echo "----------"
    python pocs/locks/fasteners_1.py --offset 1 -r ${1} & \
    python pocs/locks/fasteners_1.py -r ${1} & \
    python pocs/locks/fasteners_1.py -r ${1}
}

function help {
# Display helping message
funcs=$(introspection)
cat <<EOF
usage: $0 [<args>]

Run fasteners process locks pocs

Arguments:
    -s, --scenario      run specific scenario (${funcs})
    -d, --debug         Turn on the debug mode
    -h, --help          show this help message and exit
examples:
    $0 --scenario=1
EOF
}

function introspection {
    script=$(basename "$0")
    dirname=$(dirname "$0")
    ignore="introspection|help|grep"
    funcs=$(cat ${dirname}/${script} | \
        grep "function" | \
        egrep -v -E "${ignore}" | \
        awk -F " " '{print $2 ","}')
    # removing the final comat who is useless
    echo ${funcs:0:${#func}-1}
}

REPEAT=10
# Parse command line user inputs
for i in "$@"
do
    case $i in
        # The scenario to run
        -s=*|--scenario=*)
        SCENARIO="${i#*=}"
        shift 1
        ;;
        # The number of repeat
        -r=*|--repeat=*)
        REPEAT="${i#*=}"
        shift 1
        ;;
        # Turn on the debug mode
        -d|--debug)
        set -x
        shift 1
        ;;
        # Display the helping message
        -h|--help)
        help
        exit 0
        ;;
    esac
done

if [ -n "${SCENARIO}" ]; then
    scenarios=$(echo "$(introspection)" | sed 's/,//g')
    for scenario in ${scenarios}; do
        if [ "${scenario}" = "${SCENARIO}" ]; then
            echo "execute ${SCENARIO}"
            eval ${SCENARIO} ${REPEAT}
            echo "Done!"
            exit
        fi
    done
    echo "No corresponding scenario found"
    exit 1
fi

echo "Play all scenarios"
scenarios=$(echo "$(introspection)" | sed 's/,//g')
for scenario in ${scenarios}; do
    echo "execute ${scenario}"
    eval ${scenario} ${REPEAT}
    sleep 10
done
echo "Done!"
