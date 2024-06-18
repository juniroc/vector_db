
if docker images --format milvusdb/milvus | grep -q milvusdb/milvus; then
    echo "milvusdb/milvus image exists"
else
    echo "milvusdb/milvus image does not exist"
    docker pull milvusdb/milvus
fi



