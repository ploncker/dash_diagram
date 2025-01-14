import React, { useEffect, useRef } from 'react';
import PropTypes from 'prop-types';
import { saveSvgAsPng, svgAsPngUri } from 'save-svg-as-png';

const Mermaid = (props) => {
    const { id, chart, config, className, export_trigger, setProps } = props;
    const mermaidRef = useRef(null);
    const scriptRef = useRef(null);
    const [lastExportTrigger, setLastExportTrigger] = React.useState(export_trigger);
    
    // Export function
    const generateImage = async () => {
        console.log('Starting Mermaid diagram export...');
        
        try {
            // Find the SVG element
            const svgElement = mermaidRef.current.querySelector('svg');
            if (!svgElement) {
                console.error('SVG element not found in Mermaid diagram');
                return;
            }

            // Generate timestamp for filename
            const now = new Date();
            const dateStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, "0")}-${String(now.getDate()).padStart(2, "0")}`;
            const timeStr = `${String(now.getHours()).padStart(2, "0")}${String(now.getMinutes()).padStart(2, "0")}${String(now.getSeconds()).padStart(2, "0")}`;
            const fileName = `mermaid_${dateStr}_${timeStr}.png`;

            console.log('Found SVG, preparing to export...', {
                width: svgElement.width.baseVal.value,
                height: svgElement.height.baseVal.value,
                viewBox: svgElement.getAttribute('viewBox')
            });

            // Export options
            const options = {
                scale: 2,                    // Higher quality
                backgroundColor: '#ffffff',  // White background
                encoderOptions: 1,           // Highest quality
                encoderType: 'image/png',
                fonts: [],                   // Auto-detect fonts
                excludeUnusedCss: true,      // Optimize CSS
                width: svgElement.width.baseVal.value,
                height: svgElement.height.baseVal.value
            };

            // First try to get the PNG URI to verify the conversion works
            try {
                const uri = await svgAsPngUri(svgElement, options);
                console.log('Successfully generated PNG URI');
                
                // If URI generation successful, save the file
                await saveSvgAsPng(svgElement, fileName, options);
                console.log('Export completed successfully');
            } catch (error) {
                console.error('Error during PNG conversion:', error);
                throw error;
            }

        } catch (error) {
            console.error('Error in generateImage:', error);
        }
    };

    // Watch for changes to export_trigger
    useEffect(() => {
        if (export_trigger !== lastExportTrigger) {
            console.log('Export triggered');
            generateImage();
            setLastExportTrigger(export_trigger);
            // Report back that the export was handled
            if (setProps) {
                setProps({ export_trigger: export_trigger });
            }
        }
    }, [export_trigger, lastExportTrigger, setProps]);

    // Original Mermaid initialization code
    useEffect(() => {
        const loadScript = () => {
            return new Promise((resolve, reject) => {
                if (window.mermaid) {
                    resolve();
                    return;
                }

                if (scriptRef.current) {
                    scriptRef.current.addEventListener('load', () => resolve());
                    scriptRef.current.addEventListener('error', () => reject());
                    return;
                }

                const script = document.createElement('script');
                script.src = "https://unpkg.com/mermaid@11.4.1/dist/mermaid.min.js";
                script.async = true;
                script.onload = () => resolve();
                script.onerror = () => reject();
                
                scriptRef.current = script;
                document.body.appendChild(script);
            });
        };

        const initializeMermaid = () => {
            if (!window.mermaid) return false;
            
            const defaultConfig = {
                startOnLoad: true,
                theme: 'default',
                securityLevel: 'loose'
            };
            
            window.mermaid.initialize({ ...defaultConfig, ...config });
            return true;
        };

        const renderDiagram = async () => {
            if (!mermaidRef.current || !chart) return;

            try {
                await loadScript();
                
                if (!initializeMermaid()) {
                    throw new Error('Failed to initialize Mermaid');
                }

                mermaidRef.current.innerHTML = '';

                const element = document.createElement('pre');
                element.className = 'mermaid';
                element.textContent = chart;
                mermaidRef.current.appendChild(element);

                await window.mermaid.run({
                    nodes: [element]
                });

            } catch (err) {
                console.error('Mermaid rendering error:', err);
                if (mermaidRef.current) {
                    mermaidRef.current.innerHTML = `
                        <div style="color: red; padding: 10px; border: 1px solid red; border-radius: 4px;">
                            Error rendering diagram: ${err.message || 'Unknown error'}
                        </div>`;
                }
            }
        };

        renderDiagram();

        return () => {
            if (scriptRef.current && scriptRef.current.parentNode) {
                scriptRef.current.parentNode.removeChild(scriptRef.current);
                scriptRef.current = null;
            }
        };
    }, [chart, config]);

    return (
        <div 
            id={id}
            className={className}
            ref={mermaidRef}
            style={{ 
                width: '100%',
                minHeight: '100px',
                backgroundColor: '#ffffff',
                padding: '20px'
            }}
        />
    );
};

Mermaid.defaultProps = {
    className: '',
    config: null,
    export_trigger: 0
};

Mermaid.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string.isRequired,

    /**
     * The Mermaid diagram definition in text format.
     */
    chart: PropTypes.string.isRequired,

    /**
     * Optional configuration object for Mermaid initialization.
     */
    config: PropTypes.object,

    /**
     * Optional CSS class name for the container div.
     */
    className: PropTypes.string,

    /**
     * Trigger for exporting the diagram as PNG.
     */
    export_trigger: PropTypes.number,

    /**
     * Dash callback setter
     */
    setProps: PropTypes.func
};

export default Mermaid;
