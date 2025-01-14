/**
 * A Reactflow diagram component for Dash.
 * Renders ReactFlow diagrams from text definitions using ReactFlow version 10 (Dash does not support React version for ReactFlow version 12).
 */
 
import React, { Component, useCallback, useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import ReactFlow, { 
    MiniMap, 
    Controls, 
    Background, 
    ReactFlowProvider, 
    useReactFlow,
    getRectOfNodes,
    getTransformForBounds 
} from 'react-flow-renderer';
import { toPng } from 'html-to-image';

const FlowWithDownload = ({ id, nodes, edges, style, export_trigger, ...props }) => {
    const reactFlowInstance = useReactFlow();
    const [lastExportTrigger, setLastExportTrigger] = useState(export_trigger);

    const generateImage = useCallback(() => {
        console.log('Starting image generation process...');
        
        if (!reactFlowInstance) {
            console.error('Flow instance not ready');
            return;
        }

        try {
            const flowNodes = reactFlowInstance.getNodes();
            const nodesBounds = getRectOfNodes(flowNodes);
            console.log('Node bounds:', nodesBounds);

            const imageWidth = Math.max(nodesBounds.width + 200, 800);
            const imageHeight = Math.max(nodesBounds.height + 200, 600);
            
            const transform = getTransformForBounds(
                nodesBounds,
                imageWidth,
                imageHeight,
                0.5,
                2
            );

            const flowElement = document.querySelector('.react-flow__viewport');
            if (!flowElement) {
                console.error('Flow element not found');
                return;
            }

            toPng(flowElement, {
                backgroundColor: '#f8f8fa',
                width: imageWidth,
                height: imageHeight,
                style: {
                    width: String(imageWidth),
                    height: String(imageHeight),
                    transform: `translate(${transform[0]}px, ${transform[1]}px) scale(${transform[2]})`,
                }
            })
            .then((dataUrl) => {
                const now = new Date();
                const dateStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, "0")}-${String(now.getDate()).padStart(2, "0")}`;
                const timeStr = `${String(now.getHours()).padStart(2, "0")}${String(now.getMinutes()).padStart(2, "0")}${String(now.getSeconds()).padStart(2, "0")}`;
                const fileName = `flowchart_${dateStr}_${timeStr}.png`;

                const a = document.createElement("a");
                a.setAttribute("download", fileName);
                a.setAttribute("href", dataUrl);
                a.click();
                console.log('Export completed successfully');
            })
            .catch((error) => {
                console.error('Error in toPng conversion:', error);
            });
        } catch (error) {
            console.error('Error in generateImage:', error);
        }
    }, [reactFlowInstance]);

    // Watch for changes to export_trigger and trigger export
    useEffect(() => {
        if (export_trigger !== lastExportTrigger) {
            console.log('Export triggered');
            generateImage();
            setLastExportTrigger(export_trigger);
            // Report back that the export was triggered
            if (props.setProps) {
                props.setProps({ export_trigger: export_trigger });
            }
        }
    }, [export_trigger, generateImage, lastExportTrigger, props.setProps]);

    return (
        <div id={id} style={{ width: '100%', height: '100%', position: 'relative' }}>
            <ReactFlow
                nodes={nodes}
                edges={edges}
                {...props}
            >
                <Controls />
                <MiniMap />
                <Background />
            </ReactFlow>
        </div>
    );
};

export default class Reactflow extends Component {
    render() {
        const {
            id,
            nodes,
            edges,
            node_types,
            edge_types,
            min_zoom,
            max_zoom,
            default_zoom,
            default_position,
            fit_view,
            snap_to_grid,
            snap_grid,
            nodes_draggable,
            nodes_connectable,
            elements_selectable,
            pan_on_drag,
            pan_on_scroll,
            zoom_on_scroll,
            zoom_on_pinch,
            connection_mode,
            style,
            className,
            export_trigger,
            setProps
        } = this.props;

        return (
            <div style={style}>
                <ReactFlowProvider>
                    <FlowWithDownload 
                        id={id}
                        nodes={nodes}
                        edges={edges}
                        nodeTypes={node_types}
                        edgeTypes={edge_types}
                        minZoom={min_zoom}
                        maxZoom={max_zoom}
                        defaultZoom={default_zoom}
                        defaultPosition={default_position}
                        fitView={fit_view}
                        snapToGrid={snap_to_grid}
                        snapGrid={snap_grid}
                        nodesDraggable={nodes_draggable}
                        nodesConnectable={nodes_connectable}
                        elementsSelectable={elements_selectable}
                        panOnDrag={pan_on_drag}
                        panOnScroll={pan_on_scroll}
                        zoomOnScroll={zoom_on_scroll}
                        zoomOnPinch={zoom_on_pinch}
                        connectionMode={connection_mode}
                        className={className}
                        export_trigger={export_trigger}
                        onNodesChange={(changes) => {
                            if (setProps) {
                                setProps({ nodes_change: changes });
                            }
                        }}
                        onEdgesChange={(changes) => {
                            if (setProps) {
                                setProps({ edges_change: changes });
                            }
                        }}
                        onConnect={(params) => {
                            if (setProps) {
                                setProps({ connect: params });
                            }
                        }}
                        onNodeClick={(event, node) => {
                            if (setProps) {
                                setProps({ clicked_node: node });
                            }
                        }}
                        onEdgeClick={(event, edge) => {
                            if (setProps) {
                                setProps({ clicked_edge: edge });
                            }
                        }}
                    />
                </ReactFlowProvider>
            </div>
        );
    }
}

Reactflow.defaultProps = {
    min_zoom: 0.5,
    max_zoom: 2,
    default_zoom: 1,
    default_position: [0, 0],
    fit_view: false,
    snap_to_grid: false,
    snap_grid: [15, 15],
    nodes_draggable: true,
    nodes_connectable: true,
    elements_selectable: true,
    pan_on_drag: true,
    pan_on_scroll: false,
    zoom_on_scroll: true,
    zoom_on_pinch: true,
    connection_mode: 'strict',
    nodes_change: null,
    edges_change: null,
    connect: null,
    clicked_node: null,
    clicked_edge: null,
    export_trigger: 0
};

Reactflow.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Array of node objects with positions and data.
     */
    nodes: PropTypes.arrayOf(PropTypes.object).isRequired,

    /**
     * Array of edge objects that connect nodes.
     */
    edges: PropTypes.arrayOf(PropTypes.object).isRequired,

    /**
     * Latest nodes change event data
     */
    nodes_change: PropTypes.array,

    /**
     * Latest edges change event data
     */
    edges_change: PropTypes.array,

    /**
     * Latest connection event data
     */
    connect: PropTypes.object,

    /**
     * Latest clicked node data
     */
    clicked_node: PropTypes.object,

    /**
     * Latest clicked edge data
     */
    clicked_edge: PropTypes.object,

    /**
     * Custom node types object.
     */
    node_types: PropTypes.object,

    /**
     * Custom edge types object.
     */
    edge_types: PropTypes.object,

    /**
     * Minimum zoom level.
     */
    min_zoom: PropTypes.number,

    /**
     * Maximum zoom level.
     */
    max_zoom: PropTypes.number,

    /**
     * Default zoom level.
     */
    default_zoom: PropTypes.number,

    /**
     * Default position of the viewport [x, y].
     */
    default_position: PropTypes.arrayOf(PropTypes.number),

    /**
     * Fit the viewport to the nodes on first render.
     */
    fit_view: PropTypes.bool,

    /**
     * Enable snapping nodes to grid.
     */
    snap_to_grid: PropTypes.bool,

    /**
     * Grid size for snapping [x, y].
     */
    snap_grid: PropTypes.arrayOf(PropTypes.number),

    /**
     * Allow nodes to be dragged.
     */
    nodes_draggable: PropTypes.bool,

    /**
     * Allow nodes to be connected.
     */
    nodes_connectable: PropTypes.bool,

    /**
     * Allow elements to be selected.
     */
    elements_selectable: PropTypes.bool,

    /**
     * Enable panning when dragging on the canvas.
     */
    pan_on_drag: PropTypes.bool,

    /**
     * Enable panning when scrolling.
     */
    pan_on_scroll: PropTypes.bool,

    /**
     * Enable zooming when scrolling.
     */
    zoom_on_scroll: PropTypes.bool,

    /**
     * Enable zooming on pinch.
     */
    zoom_on_pinch: PropTypes.bool,

    /**
     * Connection mode: 'strict' (only source to target) or 'loose'.
     */
    connection_mode: PropTypes.oneOf(['strict', 'loose']),

    /**
     * CSS styles to apply to the container.
     */
    style: PropTypes.object,

    /**
     * Additional CSS class names.
     */
    className: PropTypes.string,

    /**
     * Trigger for exporting the flow diagram as PNG. Increment to trigger export.
     */
    export_trigger: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
