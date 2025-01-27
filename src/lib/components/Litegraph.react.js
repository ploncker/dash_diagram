import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { LGraph, LGraphCanvas, LiteGraph } from 'litegraph.js';
import 'litegraph.js/css/litegraph.css';

/**
 * LiteGraph component for creating graph-based node editors in Dash.
 * Based on litegraph.js library.
 */
export default class Litegraph extends Component {
    constructor(props) {
        super(props);
        
        this.canvasRef = React.createRef();
        this.graph = null;
        this.canvas = null;
        
        console.log("Component initialized");
        /*this.serializeGraph = this.serializeGraph.bind(this);*/
    }

    componentDidMount() {
        this.initGraph();
        /*this.canvas.graph.serialize = () => this.graph.serialize();*/
        console.log("componentDidMount initialized");
        /*this.props.setProps({ serializeGraph: () => this.handleSerialize() });*/
        // Register the event function from Dash
        if (this.props.setProps) {
            this.props.setProps({ serializeGraph: this.handleSerialize });
        }
        console.log("serializeGraph initialized");
    }
    
    
    handleSerialize = () => {
        if (!this.graph) {
            console.warn("No graph initialized");
            return;
        }

        const serializedData = this.graph.serialize();
        console.log("📢 Serialized Data:", serializedData);

        if (this.props.setProps) {
            this.props.setProps({ serializedGraph: serializedData });
        }
    };
    
    /*handleSerialize() {
        console.log("Serialize requested");
        if (this.graph) {
            const data = this.graph.serialize();
            console.log("Graph data:", data);
            this.props.setProps({
                serializedGraph: data
            });
        }
    }*/
    

    componentDidUpdate(prevProps) {
        // Handle updates to nodes or connections
        if (prevProps.nodes !== this.props.nodes) {
            this.updateNodes();
        }
        
        // Handle size updates
        if (prevProps.width !== this.props.width || prevProps.height !== this.props.height) {
            if (this.canvas) {
                this.canvas.resize(this.props.width, this.props.height);
            }
        }
        
        // Check if triggerSerialize changed and call serialization
        /*if (prevProps.triggerSerialize !== this.props.triggerSerialize) {
            console.log("trigger:", this.props.triggerSerialize); 
            this.handleSerialize();
        }*/
        
        if (this.props.serialize && !prevProps.serialize) {
            this.handleSerialize();
            this.props.setProps({serialize: false});
        }
    }
    
    

    componentWillUnmount() {
        // Cleanup
        if (this.graph) {
            this.graph.stop();
            this.graph.clear();
        }
        if (this.canvas) {
            this.canvas.clear();
        }
    }

    initGraph() {
        const { id, width, height } = this.props;
        
        if (!this.canvasRef.current) {
            return;
        }

        // Set initial canvas dimensions
        this.canvasRef.current.width = width;
        this.canvasRef.current.height = height;
        
        // Create new graph
        this.graph = new LGraph();
        
        // Initialize canvas with graph
        this.canvas = new LGraphCanvas(`#${id}`, this.graph);
        
        // Configure canvas
        if (this.canvas) {
            this.canvas.resize(width, height);
        
            // Add nodes from props
            this.updateNodes();
            
            // Start graph execution if autostart is true
            if (this.props.autostart) {
                this.graph.start();
            }
            
            // Setup graph events
            this.setupPointerEvents();
        }
        
        // In your React component's initGraph function
        // here we override onShowNodePanel to prevent showing the panel
        this.canvas.onShowNodePanel = () => {
            // Do nothing
            return false; // Prevent default panel
        };
    }

    updateNodes() {
        if (!this.graph || !this.props.nodes) return;
        
        // Clear existing nodes
        this.graph.clear();
        
        // Add nodes from props
        this.props.nodes.forEach(nodeData => {
            const node = LiteGraph.createNode(nodeData.type);
            if (node) {
                node.pos = nodeData.pos || [0, 0];
                if (nodeData.properties) {
                    Object.assign(node.properties, nodeData.properties);
                }
                this.graph.add(node);
            }
        });
        
        // Update connections
        if (this.props.connections) {
            this.props.connections.forEach(conn => {
                const originNode = this.graph.getNodeById(conn.origin_id);
                const targetNode = this.graph.getNodeById(conn.target_id);
                if (originNode && targetNode) {
                    originNode.connect(conn.origin_slot, targetNode, conn.target_slot);
                }
            });
        }
    }

    
    
    setupPointerEvents() {
        if (!this.graph || !this.canvas) return;


        this.graph.onNodeAdded = (node) => {
            if (this.props.setProps) {
                const nodeData = {
                    id: node.id,
                    type: node.type,
                    pos: node.pos
                };
                this.props.setProps({
                    lastNodeAdded: nodeData,
                    onNodeAdded: null
                });
            }
        };

        // Handle node selection
        this.canvas.onNodeDblClicked = (node, event) => {
            console.log("Node double clicked:", node);
            if (this.props.setProps) {
                const nodeData = node ? {
                    id: node.id,
                    type: node.type,
                    pos: node.pos,
                    properties: node.properties || {},
                    title: node.title,
                    inputs: node.inputs?.map(input => ({
                        name: input.name,
                        type: input.type,
                        link: input.link
                    })) || [],
                    outputs: node.outputs?.map(output => ({
                        name: output.name,
                        type: output.type,
                        links: output.links
                    })) || []
                } : null;
                
                this.props.setProps({
                    nodeDblClicked: nodeData,
                    onNodeDblClicked: null
                });
            }
        };
        

        this.graph.onNodeRemoved = (node) => {
            if (this.props.setProps) {
                this.props.setProps({
                    lastNodeRemoved: node.id,
                    onNodeRemoved: null
                });
            }
        };

        this.graph.onConnectionChange = (nodeOutput, nodeInput, event) => {
            if (this.props.setProps) {
                const pointerEvent = event ? createPointerEvent('pointerup', event) : null;
                const connectionData = {
                    output: nodeOutput?.id,
                    input: nodeInput?.id,
                    event: pointerEvent
                };
                this.props.setProps({
                    lastConnectionChange: connectionData,
                    onConnectionChange: null
                });
            }
        };
        
        /*useEffect(() => {
            if (props.serialize) {
                handleSerialize(); // This will trigger onSerialize
                props.setProps({serialize: false}); // Reset trigger
            }
        }, [props.serialize]);*/
        
        // Add serialize handler to the graph itself 
        /*this.graph.onSerialize = (data, event) => {
            console.log("We got here!!", data)
            if (!this.graph) {
                console.warn("No graph initialized");
                return null;
            }
            const serializedData = this.graph.serialize();
            console.log("Serialized Graph Data:", serializedData);  // <-- Debugging Log
        
            if (this.props.setProps) {
                console.log("setProps is available");  // <-- Confirm setProps is defined
                this.props.setProps({ serializedGraph: serializedData });
            } else {
                console.log("setProps is NOT available");
            }
        
            return serializedData;
        };*/
        
        
        /*useEffect(() => {
            if (props.triggerSerialize) {
                serializeGraph();
                props.setProps({triggerSerialize: false});
            }
        }, [props.triggerSerialize]);*/

        // Add serialize handler
        /*this.graph.onSerialize = () => {
             if (!this.graph) {
                 console.warn("No graph initialized");
                 return null;
             }
             const serializedData = this.graph.serialize();
             if (this.props.setProps) {
                 this.props.setProps({
                     serializedGraph: serializedData
                 });
             }
             return serializedData;
        };*/
        
        /*this.graph.onSerialize = () => {
            if (!this.graph) {
                console.warn("No graph initialized");
                return null;
            }
            const serializedData = this.graph.serialize();
            console.log("Serialized_Graph:", serializedData);
            
            if (this.props.setProps) {
                console.log("setProps is available");
                this.props.setProps({ serializedGraph: serializedData });
            } else {
                console.warn("setProps is NOT available");
            }
    
            return serializedData;
        };*/
        
        /*// Add serialize handler to the graph itself
        this.graph.onSerialize = (data, event) => {
            console.log("OnSerialize called", data, this.graph);
            if (this.props.setProps) {
                this.props.setProps({
                    serializedGraph: data 
                });
            }
            return data;
        };*/
        
        
        
        
        /*// Add serialize handler
        this.graph.onSerialize = () => {
            console.log("onSerialize reached");
            if (!this.graph) {
                console.log("No graph initialized");
                return null;
            }
            console.log("serialising data");
            const serializedData = this.graph.serialize();
            if (this.props.setProps) {
                this.props.setProps({
                    serializedGraph: serializedData,
                });
            }
            return serializedData;
        };*/
        
        
    }

    updateNodes() {
        if (!this.graph || !this.props.nodes) return;
        
        this.graph.clear();
        
        this.props.nodes.forEach(nodeData => {
            const node = LiteGraph.createNode(nodeData.type);
            if (node) {
                node.pos = nodeData.pos || [0, 0];
                if (nodeData.properties) {
                    Object.assign(node.properties, nodeData.properties);
                }
                this.graph.add(node);
            }
        });
        
        if (this.props.connections) {
            this.props.connections.forEach(conn => {
                const originNode = this.graph.getNodeById(conn.origin_id);
                const targetNode = this.graph.getNodeById(conn.target_id);
                if (originNode && targetNode) {
                    originNode.connect(conn.origin_slot, targetNode, conn.target_slot);
                }
            });
        }
    }


    render() {
        const { id, width, height, className } = this.props;
        
        return (
            <div style={{ width: width, height: height }}>
                <canvas
                    ref={this.canvasRef}
                    id={id}
                    className={className}
                    style={{ 
                        width: '100%',
                        height: '100%',
                        position: 'relative',
                        touchAction: 'none',
                        border: '1px solid #000'
                    }}
                />
            </div>
        );
    }
}

Litegraph.defaultProps = {
    width: 1024,
    height: 720,
    autostart: true,
    nodes: [],
    connections: [],
    serialize: false,
    //selectedNode: null,
    lastNodeAdded: null,
    lastNodeRemoved: null,
    lastConnectionChange: null,
    onNodeAdded: null,
    onNodeRemoved: null,
    onConnectionChange: null,
    onNodeDblClicked: null,
    /*triggerSerialize: 0  // Default value*/
    /*onSerialize: null,*/
    
};

Litegraph.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string.isRequired,

    /**
     * Canvas width in pixels
     */
    width: PropTypes.number,

    /**
     * Canvas height in pixels
     */
    height: PropTypes.number,

    /**
     * Whether to automatically start graph execution
     */
    autostart: PropTypes.bool,

    /**
     * Array of node configurations
     */
    nodes: PropTypes.arrayOf(PropTypes.shape({
        type: PropTypes.string.isRequired,
        pos: PropTypes.arrayOf(PropTypes.number),
        properties: PropTypes.object
    })),

    /**
     * Array of connection configurations
     */
    connections: PropTypes.arrayOf(PropTypes.shape({
        origin_id: PropTypes.number.isRequired,
        target_id: PropTypes.number.isRequired,
        origin_slot: PropTypes.number.isRequired,
        target_slot: PropTypes.number.isRequired
    })),

    /**
     * Additional CSS class for the canvas element
     */
    className: PropTypes.string,

    /**
     * Last node that was added
     */
    lastNodeAdded: PropTypes.object,

    /**
     * Last node that was removed
     */
    lastNodeRemoved: PropTypes.number,

    /**
     * Last connection change that occurred
     */
    lastConnectionChange: PropTypes.object,
    
    /**
     * Serialised data
     */
    serializedGraph: PropTypes.object,

    /**
     * Temporary storage for node added event
     */
    onNodeAdded: PropTypes.object,

    /**
     * Temporary storage for node removed event
     */
    onNodeRemoved: PropTypes.number,

    /**
     * Temporary storage for connection change event
     */
    onConnectionChange: PropTypes.object,

    /**
     * Currently selected node and its properties
     */
    nodeDblClicked: PropTypes.shape({
        id: PropTypes.number,
        type: PropTypes.string,
        pos: PropTypes.arrayOf(PropTypes.number),
        properties: PropTypes.object,
        title: PropTypes.string,
        inputs: PropTypes.arrayOf(PropTypes.shape({
            name: PropTypes.string,
            type: PropTypes.string,
            link: PropTypes.any
        })),
        outputs: PropTypes.arrayOf(PropTypes.shape({
            name: PropTypes.string,
            type: PropTypes.string,
            links: PropTypes.any
        })),
        event: PropTypes.object
    }),
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
    
    /**
     * Callback triggered when a node is double-clicked.
     * Returns an object containing node data including id, type, position,
     * properties, title, inputs, outputs, and the triggering event.
     */
    onNodeDblClicked: PropTypes.func,
    
    /**
     * Serialise currently selected graph
     */
    serialize:  PropTypes.bool,
    
    
};
