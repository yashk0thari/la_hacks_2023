import { Handle, Position } from 'reactflow';

const handleStyle = { left: 10 };

function nodeContainer({ data, isConnectable }) {

    const x = JSON.parse(JSON.stringify(data));

  return (
    <div class="mainBody">
      <Handle type="target" position={Position.Top} isConnectable={isConnectable} />
      <Handle
        type="source"
        position={Position.Bottom}
        id={x["sourceHandle"]}
        style={handleStyle}
        isConnectable={isConnectable}
      />
      {/* <Handle type="source" position={Position.Bottom} id={x["sourceHandle"]} isConnectable={isConnectable} /> */}

        <div class="container">
            
                <img src="images/map@2x.png"></img>
                <span class="titleText">Random Text</span>
         
        </div>

        <div class="mainPara">
            
            <p class="textMain">

                The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps.
            
            </p>
        
        </div>

        <div class="mainLower">

            <div class="categoryOne">

                <p>category</p>

            </div>

            <div class="categoryTwo">

                <p>class</p>

            </div>

            <div class="imageCategory">

                <img src="images/Group 30@2x.png"></img>

            </div>
            

        </div>

    </div>
  );
}

export default nodeContainer;
